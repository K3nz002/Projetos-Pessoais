import logging
import os
from dotenv import load_dotenv
from telegram.ext import ApplicationBuilder

from bot.scheduler import send_daily_digest

# Logging configurado para aparecer limpo nos logs do Docker
logging.basicConfig(
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

load_dotenv()

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")


def main():
    if not TOKEN or not CHAT_ID:
        raise ValueError(
            "As variáveis de ambiente TELEGRAM_BOT_TOKEN e TELEGRAM_CHAT_ID são obrigatórias."
        )

    app = ApplicationBuilder().token(TOKEN).build()

    # Agendamento: primeira execução 10 segundos após o start, depois a cada 4 horas
    job_queue = app.job_queue
    job_queue.run_repeating(
        send_daily_digest,
        interval=14400,
        first=10,
        chat_id=CHAT_ID,
    )

    logger.info("Bot rodando... (intervalo: 4h)")
    app.run_polling()


if __name__ == "__main__":
    main()