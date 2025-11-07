from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import time, uuid

app = FastAPI(title="Lupine Rail API", version="0.1.0")

class QuoteRequest(BaseModel):
    source_currency: str
    target_currency: str
    amount: float
    corridor: Optional[str] = None
    urgency: Optional[str] = "normal"

class PayRequest(BaseModel):
    quote_id: str
    sender_ref: Optional[str] = None

_quotes = {}
_status = {}

@app.get("/health")
def health():
    return {"ok": True, "ts": int(time.time())}

@app.post("/quote")
def quote(req: QuoteRequest):
    # Mock fee/latency scoring for AU↔SG↔MY
    rate = 0.90 if req.target_currency != req.source_currency else 1.0
    fee = round(max(0.50, req.amount * 0.0025), 2)
    delivered = round(req.amount * rate - fee, 2)
    qid = str(uuid.uuid4())
    _quotes[qid] = {
        "rate": rate, "fee": fee, "delivered": delivered,
        "corridor": req.corridor or f"{req.source_currency}-{req.target_currency}",
        "urgency": req.urgency, "ts": int(time.time())
    }
    return {"quote_id": qid, **_quotes[qid]}

@app.post("/pay")
def pay(req: PayRequest):
    if req.quote_id not in _quotes:
        return {"error": "invalid_quote_id"}
    pid = str(uuid.uuid4())
    _status[pid] = {"state": "submitted", "quote": _quotes[req.quote_id], "ts": int(time.time())}
    return {"payment_id": pid, "state": _status[pid]["state"]}

@app.get("/status/{payment_id}")
def status(payment_id: str):
    if payment_id not in _status:
        return {"error": "not_found"}
    # flip to settled after a short mock lifecycle
    st = _status[payment_id]
    if st["state"] == "submitted":
        st["state"] = "processing"
    elif st["state"] == "processing":
        st["state"] = "settled"
    return {"payment_id": payment_id, "state": st["state"], "quote": st["quote"]}
