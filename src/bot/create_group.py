from . import dispatcher
from ..database import Session, User, Group, Permission, Perm, add_to_database
from telegram.ext import CommandHandler


def create_group(update, context):
    session = Session()

    tg_id = update.effective_user.id
    user = session.query(User).filter_by(tg_id=tg_id).first()
    if user is None:
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=(
                "Пользователь не найден в системе. "
                "Попробуйте воспользоваться командой '/start'."
            ),
        )
        Session.remove()
        return

    if context.args is None or context.args == []:
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Название группы не может быть пустым.",
        )
        Session.remove()
        return

    group_title = " ".join(context.args)
    if group_title == "":
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Название группы не может быть пустым.",
        )
        Session.remove()
        return

    group = Group(title=group_title)

    perm = Permission(group=group, user=user, perm=Perm.all())

    if not add_to_database([group, perm], session):
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=(
                "Не удалось создать группу. Попробуйте еще "
                "раз или обратитесь к администратору."
            ),
        )
    else:
        context.bot.send_message(
            chat_id=update.effective_chat.id, text="Группа успешно создана!"
        )

    Session.remove()


create_group_handler = CommandHandler("create_group", create_group)
dispatcher.add_handler(create_group_handler)
