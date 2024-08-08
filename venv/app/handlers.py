from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery, WebAppInfo
import emoji


import app.keyboard as kb
router = Router ()




# При старте пишет сообщение
@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(f'\u2708\ufe0f Добрый день, {message.from_user.first_name}!'
                         f' Добро пожаловать на курс "Практика создания электронного курса в LMS MOODLE" ',
                        reply_markup=kb.settings)




# грузим фотографию на сервер телеграма и получаем айди
@router. message(F.photo)
async def get_photo(message: Message):
    await message.answer(f'ID фото: {message.photo[-1].file_id}')


@router.message(Command('get_photo'))
async def get_photo(message: Message):
    await message.answer_photo(photo='AgACAgIAAxkBAAIBeWanm9xcliCGe51h5NfgTwY8oX2oAAJt4jEbrDU4SQg6Y9OEEI1mAQADAgADdwADNQQ',caption='ololo')


@router.message(F.document)
async def get_document(message: Message):
    await message.answer(f'ID документа: {message.document.file_id}')


@router.message(Command('get_document'))
async def get_document(message: Message):
    await message.answer_document(document='BQACAgIAAxkBAAIBe2anm-lBweW5039zRMSW-K9kaj2DAAKHWQACrDU4SYwgibi2fm4GNQQ',caption='ololo')


@router.message(F.video)
async def get_file(message: Message):
    await message.answer_video(f'ID документа: {message.video.file_id}')


@router.message(Command('get_video'))
async def get_video(message: Message):
    await message.answer_video(video='BQACAgIAAxkBAAIBpGaonbQtNcFdyiZWvhBz0zqioOHIAAIdXAACvjhBSbxUHkWeDMjHNQQ',caption='kek')


@router.message(F.sticker)
async def get_sticker(message: Message):
    await message.answer(f'ID стикера: {message.sticker.file_id}')

@router.message(F.animation)
async def get_animation(message: Message):
    await message.answer(f'ID стикера: {message.animation.file_id}')


@router.callback_query(F.data=='course_information')
async def course_information(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer('В данном курсе рассматриваются этапы разработки электронного курса от проектирования до реализации в среде LMS MOODLE. В ходе изучения данного курса слушатели ознакомятся с методическими и практическими аспектами проектирования контента электронного курса. Подробно рассмотрены такие вопросы, как планирование работы над курсом, создание учебного контента, разработка видеолекций, работа по размещению учебного контента на курсе в среде LMS MOODLE. Для успешного освоения учебного материала, в курсе размещены подробные инструкции в текстовом и видеоформате. Для успешного освоения программы курса и закрепления знаний и навыков, слушателям предлагается выполнить практические задания. В ходе выполнения практических заданий слушатели создадут проект своего электронного курса и начнут разработку электронного курса в среде Moodle - одну из тем и общие материалы по курсу.По итогам изучения данного электронного курса слушатели получат знания и навыки, необходимые для создания электронного курса, соответствующего высоким стандартам качества.Курс предназначен для авторов-разработчиков электронных курсов Передовой инженерной школы.', reply_markup=kb.settings)



@router.callback_query(F.data=='promovideo')
async def promo(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer('промовидео')


@router.callback_query(F.data=='theme1')
async def quality(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer('В данной теме Вы ознакомитесь с общими принципами проектирования электронного курса и с критериями качества электронного курса.'
                                  'По итогам освоения данной темы вы узнаете об основных принципах эффективного электронного обучения на нём, научитесь определять сильные и слабые стороны отдельных курсов."',reply_markup=kb.themes1)


@router.callback_query(F.data=='obozn')
async def obozn(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer(emoji.emojize(':clapper_board: - Видеоролик \n:laptop: - Презентация \n:memo: - Теоретический материал \n:page_facing_up: - скачать документ'
                                                ' \n:red_exclamation_mark: - Информация \n:globe_with_meridians: - дополнительные материалы '
                                                '\n:left_arrow: - Вернуться в предыдщую тему \n:right_arrow: - перейти в следующую тему \n:up_arrow: - вернуться в главное меню'), reply_markup=kb.settings)



@router.callback_query(F.data == 'vopros')
async def vopros(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer('Написать в Telegram https://t.me/UniverSoldat', reply_markup=kb.settings)




@router.callback_query(F.data == 'quality')
async def quality1(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer('ссылка на файл Критерии качества электронного курса')

@router.callback_query(F.data == 'method_recom')
async def tema2(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer('По итогам изучения темы Вы научитесь планированию разработки курса, а также создавать содержание курса.', reply_markup=kb.themes2)

@router.callback_query(F.data == 'etap')
async def etap(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer('Этапы разработки электронного курса', web_ap=WebAppInfo(url='https://moodle.kai.ru/mod/page/view.php?id=33432'))

@router.callback_query(F.data == 'planirov')
async def etap(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer('Планирование')


@router.callback_query(F.data == 'blank')
async def blank(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer('Бланк таблицы со структурой онлайн-курса')

@router.callback_query(F.data == 'table')
async def table(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer('Пример заполнения таблицы структуры курса')

@router.callback_query(F.data == 'plan')
async def plan(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer('Пример понедельного плана обучения')

@router.callback_query(F.data == 'design')
async def design(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer('Дополнительный материал. Что такое педагогический дизайн?')

@router.callback_query(F.data == 'mero')
async def mero(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer('Разработка контрольных мероприятий')

@router.callback_query(F.data == 'bloom1')
async def bloom1(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer('Дополнительный материал. Таксономия Блума')


@router.callback_query(F.data == 'bloom2')
async def bloom2(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer('Дополнительный материал. Практическое применение таксономии Блума при проектировании электронных курсов')

@router.callback_query(F.data == 'lection')
async def lection(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer('Разработка лекционных материалов (текст, видеолекция)')

@router.callback_query(F.data == 'promo')
async def promo(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer('Создание промо-ролика')

@router.callback_query(F.data == 'material')
async def metod(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer('Разработка методических материалов (по курсу в целом и для каждой темы)')

@router.callback_query(F.data == 'theme3')
async def lectionvideo(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer('В данной теме рассмотрены следующие вопросы: 1. Знакомство со студией Jalinga КНИТУ-КАИ;'
                                  '2. Создание скринкастов (запись экрана) с помощью программ "OBS STUDIO", "ISPRING FREE CAM", "OCAM SCREEN RECORDER".'
                                  'По итогам изучения темы Вы ознакомитесь со студией Jalinga КНИТУ-КАИ. Научитесь записывать скринкасты (запись с экрана) с помощью разных программ, используя шаблон оформления презентации. '
                                  'В данной теме рекомендуется просмотреть видеоинструкции и прочитать текстовые инструкции.', reply_markup=kb.themes3)

@router.callback_query(F.data == 'pred1')
async def predquality(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer('Вернуться к предыдущей теме "Критерии качества электронного курса"',
                                      reply_markup=kb.themes1)


@router.callback_query(F.data == 'glav1')
async def glavmenu(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer('Главное меню', reply_markup=kb.settings)


@router.callback_query(F.data == 'presentation')
async def presentation(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer('Видео про студию Jalinga')

@router.callback_query(F.data == 'jalinga')
async def jalinga1(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer('Что такое Jalinga?')

@router.callback_query(F.data == 'touchboard')
async def jalinga2(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer('Работа с Touchboard Jalinga')

@router.callback_query(F.data == 'screen_obs1')
async def screencast11(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer('Вы научитесь записывать скринкаст с помощью программы "OBS STUDIO"')


@router.callback_query(F.data == 'screen_obs')
async def screencast1(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer('Вы научитесь записывать скринкаст с помощью программы "OBS STUDIO"')

@router.callback_query(F.data == 'screen_ocam1')
async def screencast22(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer(
            'В данном видео Вы научитесь записывать скринкаст с помощью программы "OCAM SCREEN RECORDER"')

@router.callback_query(F.data == 'screen_ocam')
async def screencast2(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer('В данном видео Вы научитесь записывать скринкаст с помощью программы "OCAM SCREEN RECORDER"')


@router.callback_query(F.data == 'screen_ispring1')
async def screencast33(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer('Вы научитесь записывать скринкаст с помощью программы "ISPRING FREE CAM"')

@router.callback_query(F.data == 'screen_ispring')
async def screencast3(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer('Вы научитесь записывать скринкаст с помощью программы "ISPRING FREE CAM"')

@router.callback_query(F.data == 'moodle')
async def moodle(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer('В данном видео Вы научитесь создавать и настраивать курс на платформе https://moodle.kai.ru/', reply_markup=kb.themes4)

@router.callback_query(F.data == 'pred2')
async def predmethod(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer('Вернуться к предыдущей теме "Методические рекомендации по проектированию контента электронного курса"',reply_markup=kb.themes2)


@router.callback_query(F.data == 'pred3')
async def predmethod(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer('Создание видеолекций для электронного курса"',reply_markup=kb.themes3)


@router.callback_query(F.data == 'info1')
async def perehod(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer('В данной теме Вы изучите элементы для работы с информацией', reply_markup=kb.themes5)


@router.callback_query(F.data == 'file1')
async def file1(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer('Вы научитесь создавать и настраивать элемент "Файл"')

@router.callback_query(F.data == 'file2')
async def file2(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer('Вы научитесь создавать и настраивать элемент "Файл"')

@router.callback_query(F.data == 'map1')
async def map1(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer('Вы научитесь создавать и настраивать элемент "Страница"')

@router.callback_query(F.data == 'map2')
async def map2(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer('Вы научитесь создавать и настраивать элемент "Страница"')

@router.callback_query(F.data == 'map3')
async def map3(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer('Работа с элементом "Страница"')

@router.callback_query(F.data == 'book1')
async def book1(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer('Вы научитесь создавать и настраивать элемент "Книга"')

@router.callback_query(F.data == 'book2')
async def book2(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer('Вы научитесь создавать и настраивать элемент "Книга"')

@router.callback_query(F.data == 'lection1')
async def lection1(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer('Вы научитесь создавать и настраивать элемент "Лекция"')

@router.callback_query(F.data == 'lection2')
async def lection2(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer('Вы научитесь создавать и настраивать элемент "Лекция"')

@router.callback_query(F.data == 'lection3')
async def lection3(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer('Вы научитесь добавлять контент в элемент"Лекция"')

@router.callback_query(F.data == 'papka1')
async def papka1(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer('Вы научитесь создавать и настраивать элемент "Папка"')

@router.callback_query(F.data == 'papka2')
async def papka2(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer('Вы научитесь создавать и настраивать элемент "Папка"')

@router.callback_query(F.data == 'ebs_lan1')
async def ebs_lan1(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer('Вы научитесь создавать и настраивать элемент "ЭБС Лань"')

@router.callback_query(F.data == 'ebs_lan2')
async def ebs_lan2(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer('Вы научитесь создавать и настраивать элемент "ЭБС Лань"')



@router.callback_query(F.data == 'info2')
async def inter(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer('В данной теме Вы изучите интерактивные элементы курса',reply_markup=kb.themes6 )

@router.callback_query(F.data == 'pred4')
async def pred4(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer('Начало работы в системе MOODLE',reply_markup=kb.themes4 )



@router.callback_query(F.data == 'zadanie1')
async def zadanie1(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer('Создание и настройка элемента "Задание"')


@router.callback_query(F.data == 'zadanie')
async def zadanie(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer('Создание и настройка элемента "Задание"')

@router.callback_query(F.data == 'test')
async def test(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer('Создание и настройка элемента "Тест"')

@router.callback_query(F.data == 'verno')
async def verno(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer('Создание тестового вопроса типа "Верно/неверно"')

@router.callback_query(F.data == 'mnvibor')
async def mnvibor(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer('Создание тестового вопроса типа "Множественный выбор"')

@router.callback_query(F.data == 'korotvet')
async def korotvet(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer('Создание тестового вопроса типа "Короткий ответ"')

@router.callback_query(F.data == 'nasoot')
async def nasootv(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer('Создание тестового вопроса типа "На соответствие"')

@router.callback_query(F.data == 'chisl')
async def chisl(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer('Создание тестового вопроса типа "Числовой"')

@router.callback_query(F.data == 'vichisl')
async def vichisl(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer('Создание тестового вопроса типа "Вычисляемый"')

@router.callback_query(F.data == 'esse')
async def esse(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer('Создание тестового вопроса типа "Эссе"')

@router.callback_query(F.data == 'slova')
async def propslov(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer('Создание тестового вопроса типа "Выбор пропущенных слов"')

@router.callback_query(F.data == 'text')
async def perettext(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer('Создание тестового вопроса типа "Перетаскивание в текст"')

@router.callback_query(F.data == 'marker')
async def marker(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer('Создание тестового вопроса типа "Перетаскивание маркеров"')

@router.callback_query(F.data == 'izobr')
async def izobrperet(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer('Создание тестового вопроса типа "Перетаскивание на изображение"')

@router.callback_query(F.data == 'cloze')
async def clozee(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer('Создание табличных задач с помощью тестового вопроса типа "Вложенные ответы (cloze)"')

@router.callback_query(F.data == 'mnvich')
async def mnvichisl(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer(
            'Создание тестового вопроса типа "Множественный вычисляемый"')

@router.callback_query(F.data == 'prostvich')
async def prvichisl(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer('Создание тестового вопроса типа "Простой вычисляемый" ')

@router.callback_query(F.data == 'gloss1')
async def glosss1(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer('Создание и настройка элемента "Глоссарий" ')

@router.callback_query(F.data == 'gloss')
async def glosss(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer('Создание и настройка элемента "Глоссарий" ')

@router.callback_query(F.data == 'organiz')
async def elementorg(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer('В данной теме Вы научитесь пользоваться элементами для организации взаимодействия между обучающимся ', reply_markup=kb.themes7)


@router.callback_query(F.data == 'informationn')
async def informationn(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer('Элементы для работы с информацией',
                                      reply_markup=kb.themes5)


@router.callback_query(F.data == 'forum')
async def forum(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer('Создание и настройка элемента "Форум" ')

@router.callback_query(F.data == 'chat')
async def chat(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer('Создание и настройка элемента "Чат" ')

@router.callback_query(F.data == 'dopelement')
async def dopelement(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer('Дополнительные элементы для создания курса', reply_markup=kb.themes8)

@router.callback_query(F.data == 'predelement')
async def perehod1(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer('Интерактивные элементы курса', reply_markup=kb.themes6)


@router.callback_query(F.data == 'giper')
async def giper(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer('Создание и настройка элемента "Гиперссылка" ')

@router.callback_query(F.data == 'giper')
async def giper(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer('Создание и настройка элемента "Гиперссылка" ')

@router.callback_query(F.data == 'textmedia1')
async def textmedia1(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer('Создание и настройка элемента "Текст и медиа" ')

@router.callback_query(F.data == 'textmedia')
async def textmedia(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer('Создание и настройка элемента "Текст и медиа" ')

@router.callback_query(F.data == 'bootstrap')
async def bootstrap(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer('Создание и настройка элемента "Bootstrap Elements" ')

@router.callback_query(F.data == 'expert')
async def bootstrap(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer('Экспертиза электронного курса',reply_markup=kb.themes9)

@router.callback_query(F.data == 'predelement1')
async def bootstrap(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer('Элементы для организации взаимодействия между обучающимся',reply_markup=kb.themes7)


@router.callback_query(F.data == 'expertiza')
async def expertiza(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer('Экспертиза качества электронного курса')

@router.callback_query(F.data == 'dopelements')
async def bootstrap(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer('Дополнительные материалы по курсу', reply_markup=kb.themes10)

@router.callback_query(F.data == 'elementsvzaim')
async def elementsvzaim(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer('Дополнительные элементы для создания курса', reply_markup=kb.themes8)




@router.callback_query(F.data == 'assistent')
async def assistent(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer('Документация по программе "Ассистент"')

@router.callback_query(F.data == 'interaction')
async def interaction(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer('Руководство по использованию элемента "Интерактивный контент" ')

@router.callback_query(F.data == 'opros')
async def opros(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer('Создание и настройка элемента "Опрос" ')

@router.callback_query(F.data == 'predelement2')
async def predelement2(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer('Экспертиза качества электронного курса', reply_markup=kb.themes9)




# при вводе гет фото, пользователь получает фотографию по айди или можно вставить ссылку
