import logging
from services.currency import get_usd_rate
from services.world_news import get_latest_world_news
from services.football import get_latest_football_news
from services.hltv import get_latest_hltv_news
from services.seen_news import load_seen, save_seen, filter_new

logger = logging.getLogger(__name__)


async def send_daily_digest(context):
    chat_id = context.job.chat_id
    logger.info("Iniciando envio do digest...")

    # Carrega o histórico de notícias já enviadas (com TTL de 3 dias)
    seen = load_seen()

    # Busca e filtra apenas notícias novas por categoria
    usd_info = await get_usd_rate()
    hltv_news = filter_new(
        get_latest_hltv_news("https://www.hltv.org/rss/news", limit=5),
        seen, "hltv"
    )
    world_news = filter_new(
        get_latest_world_news("https://admin.cnnbrasil.com.br/feed/", limit=5),
        seen, "world"
    )
    football_news = filter_new(
        get_latest_football_news("https://www.espn.com.br/rss", limit=5),
        seen, "football"
    )

    # Se não há nenhuma novidade, não envia nada
    if not any([hltv_news, world_news, football_news]):
        logger.info("Nenhuma novidade encontrada. Digest não enviado.")
        return

    # Monta a mensagem — omite seções sem novidades
    msg = f"📊 *Resumo do Dia*\n\n{usd_info}\n"

    if hltv_news:
        msg += "\n🎮 *HLTV (CS2)*:\n"
        for item in hltv_news:
            msg += f"• [{item['title']}]({item['link']})\n\n"

    if world_news:
        msg += "\n🌍 *Mundo*:\n"
        for item in world_news:
            msg += f"• [{item['title']}]({item['link']})\n\n"

    if football_news:
        msg += "\n⚽ *Futebol*:\n"
        for item in football_news:
            msg += f"• [{item['title']}]({item['link']})\n\n"

    await context.bot.send_message(
        chat_id=chat_id,
        text=msg,
        parse_mode="Markdown",
        disable_web_page_preview=True,
    )

    # Persiste o estado apenas após o envio bem-sucedido
    save_seen(seen)
    logger.info(
        "Digest enviado. Novas notícias: hltv=%d, world=%d, football=%d",
        len(hltv_news), len(world_news), len(football_news),
    )
