from httpx import AsyncClient

async def get_usd_rate() -> str:
    url = "https://economia.awesomeapi.com.br/json/last/USD-BRL"
    async with AsyncClient() as client:
        response = await client.get(url)
        data = response.json().get("USDBRL", {})
        
        bid = float(data.get("bid", 0))
        pct_change = data.get("pctChange", "0")
        
        return f"💵 *Dólar (USD/BRL)*: R$ {bid:.2f} ({pct_change}%)"