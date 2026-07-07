export default {
  async fetch(req, env) {
    const cors = {"Access-Control-Allow-Origin":"*","Access-Control-Allow-Headers":"content-type","Access-Control-Allow-Methods":"GET,POST,OPTIONS"};
    if (req.method === "OPTIONS") return new Response(null,{headers:cors});
    const url = new URL(req.url);
    const json = (o,s=200)=>new Response(JSON.stringify(o),{status:s,headers:{"content-type":"application/json",...cors}});
    if (url.pathname === "/results") {
      const t = await env.VOTES.get("totals");
      return json(t ? JSON.parse(t) : {});
    }
    if (url.pathname === "/vote" && req.method === "POST") {
      let b; try { b = await req.json(); } catch { return json({ok:false},400); }
      const q = /^Q\d\d$/.test(b.q||"") ? b.q : null;
      const v = ["y","n","d"].includes(b.v) ? b.v : null;
      const uid = (b.uid||"").replace(/[^a-zA-Z0-9-]/g,"").slice(0,64);
      if (!q || !v || uid.length < 8) return json({ok:false},400);
      const key = `v:${q}:${uid}`;
      const prev = await env.VOTES.get(key);
      const totals = JSON.parse((await env.VOTES.get("totals"))||"{}");
      totals[q] = totals[q] || {y:0,n:0,d:0};
      if (prev === v) return json({ok:true,dup:true,totals:totals[q]});
      if (prev) totals[q][prev] = Math.max(0,(totals[q][prev]||0)-1);
      totals[q][v] = (totals[q][v]||0)+1;
      await env.VOTES.put(key, v);
      await env.VOTES.put("totals", JSON.stringify(totals));
      return json({ok:true,changed:!!prev,totals:totals[q]});
    }
    return new Response("BAFLP ballot worker — POST /vote {q,v,uid} · GET /results",{headers:cors});
  }
};
