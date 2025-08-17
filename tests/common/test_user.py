# tests/common/test_user.py
import pytest

@pytest.mark.parametrize(
    ("headers", "body", "status", "code"),
    [
        # هیچ Content-Type -> انتظار 415 (Unsupported Media Type)
        ({}, {}, 415, 101),

        # Content-Type = application/json اما داده‌ی نامعتبر (types اشتباه) -> انتظار 400 (validation)
        ({"Content-Type": "application/json"}, {"username": 1, "password": 1}, 400, 102),

        # Content-Type = application/json اما بدنه خالی -> انتظار 400 (missing fields)
        ({"Content-Type": "application/json"}, {}, 400, 102),
    ]
)
def test_creat_user(client, headers, body, status, code):
    # وقتی header شامل Content-Type=json هست، از json= استفاده کن تا client هدر را درست ست کند
    if headers.get("Content-Type") == "application/json":
        res = client.post("/api/v1/users", json=body, headers=headers)
    else:
        # شبیه‌سازی درخواست بدون Content-Type (ارسال داده خام)
        res = client.post("/api/v1/users", data="", headers=headers)

    assert res.status_code == status
    resp_json = res.get_json(silent=True) or {}
    assert resp_json.get("code") == code

