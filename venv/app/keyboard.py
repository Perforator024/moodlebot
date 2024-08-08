from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Информация о курсе')],
    [KeyboardButton(text='Корзина'), KeyboardButton(text='Дополнительная информация')]
], resize_keyboard=True, input_field_placeholder='Выберите пункт меню')

settings = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='\u2757 Информация о курсе', callback_data='course_information')],
    [InlineKeyboardButton(text='\ud83c\udfac Посмотреть промовидео', url='https://clck.ru/3CJpAh')],
    [InlineKeyboardButton(text='\u27a1 Тема 1: "Критерии качества электронного курса" ', callback_data='theme1')],
    [InlineKeyboardButton(text='\u27a1 Условные обозначения"', callback_data='obozn')],
    [InlineKeyboardButton(text='\ud83d\udca1 Задать вопрос специалисту по Moodle ', callback_data='vopros')]
    ])


themes1 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='\ud83d\udcdd Критерии качества электронного курса',url= 'https://clck.ru/3CKNQm', callback_data='quality')],
    [InlineKeyboardButton(text='\u27a1 Тема 2: "Методические рекомендации по проектированию контента электронного курса"', callback_data='method_recom')],
    [InlineKeyboardButton(text='\u2b06 Вернуться в главное меню', callback_data='glav1')]
    ])



themes2 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='\ud83d\udcdd 2.1 Этапы разработки электронного курса',url= 'https://clck.ru/3CKNEZ', callback_data='etap')],
    [InlineKeyboardButton(text='\ud83d\udcdd 2.2 Планирование', url= 'https://clck.ru/3CKNFX',callback_data='planirov')],
    [InlineKeyboardButton(text='\ud83d\udcc4 Бланк таблицы со структурой онлайн-курса', url='https://clck.ru/3CKNGF', callback_data='blank')],
    [InlineKeyboardButton(text='\ud83d\udcc4 Пример заполнения таблицы структуры курса',url='https://clck.ru/3CKNGy', callback_data='table')],
    [InlineKeyboardButton(text='\ud83d\udcc4 Пример понедельного плана обучения',url='https://clck.ru/3CKNHV', callback_data='plan')],
    [InlineKeyboardButton(text='\ud83c\udf10 Дополнительный материал. Что такое педагогический дизайн?',url='https://clck.ru/3CKNHv', callback_data='design')],
    [InlineKeyboardButton(text='\ud83d\udcdd 2.3 Разработка контрольных мероприятий',url='https://clck.ru/3CKNJT', callback_data='mero')],
    [InlineKeyboardButton(text='\ud83d\udcdd Дополнительный материал. Таксономия Блума',url='https://clck.ru/3Bvc8N', callback_data='bloom1')],
    [InlineKeyboardButton(text='\ud83d\udcdd Дополнительный материал. Практическое применение таксономии Блума при проектировании электронных курсов',url='https://clck.ru/3BvcBV', callback_data='bloom2')],
    [InlineKeyboardButton(text='\ud83d\udcdd 2.4 Разработка лекционных материалов (текст, видеолекция)',url='https://clck.ru/3CKNKA', callback_data='lection')],
    [InlineKeyboardButton(text='\ud83d\udcdd 2.5 Создание промо-ролика',url='https://clck.ru/3CKNKe', callback_data='promo')],
    [InlineKeyboardButton(text='\ud83d\udcdd 2.6 Разработка методических материалов (по курсу в целом и для каждой темы)',url='https://clck.ru/3CKNLS', callback_data='material')],
    [InlineKeyboardButton(text='\u27a1 Тема 3: "Создание видеолекций для электронного курса"', callback_data='theme3')],
    [InlineKeyboardButton(text='\u2b05 Тема 1: "Критерии качества электронного курса"', callback_data='pred1')],
    [InlineKeyboardButton(text='\u2b06 Вернуться в главное меню', callback_data='glav1')]
    ])





themes3 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='\ud83d\udcbb 3.1 Презентация студии Jalinga КНИТУ-КАИ',url='https://clck.ru/3BvyxA', callback_data='presentation')],
    [InlineKeyboardButton(text='\ud83c\udfac 3.1 Что такое Jalinga?',url='https://youtu.be/fbXfgINK9cw' , callback_data='jalinga')],
    [InlineKeyboardButton(text='\ud83c\udfac 3.1 Работа с Touchboard Jalinga',url='https://youtu.be/19NDKMLbA_c' , callback_data='touchboard')],
    [InlineKeyboardButton(text='\ud83c\udfac 3.2 Создание скринкаста (запись с экрана) с помощью программы "OBS STUDIO"',url='https://clck.ru/3CKFgt', callback_data='screen_obs1')],
    [InlineKeyboardButton(text='\ud83d\udcbb 3.2 Создание скринкаста (запись с экрана) с помощью программы "OBS STUDIO"',url='https://clck.ru/3BvcJY' , callback_data='screen_obs')],
    [InlineKeyboardButton(text='\ud83c\udfac 3.3 Создание скринкаста (запись с экрана) с помощью программы "OCAM SCREEN RECORDER"',url='https://clck.ru/3CKFkT', callback_data='screen_ocam1')],
    [InlineKeyboardButton(text='\ud83d\udcbb 3.3 Создание скринкаста (запись с экрана) с помощью программы "OCAM SCREEN RECORDER"',url='https://clck.ru/3BvcLx' , callback_data='screen_ocam')],
    [InlineKeyboardButton(text='\ud83c\udfac 3.4 Создание скринкаста (запись с экрана) с помощью программы "ISPRING FREE CAM"',url='https://clck.ru/3CKFnM', callback_data='screen_ispring1')],
    [InlineKeyboardButton(text='\ud83d\udcbb 3.4 Создание скринкаста (запись с экрана) с помощью программы "ISPRING FREE CAM"',url='https://clck.ru/3BvcNP' , callback_data='screen_ispring')],
    [InlineKeyboardButton(text='\u27a1 Тема 4: "Начало работы в системе MOODLE "', callback_data='moodle')],
    [InlineKeyboardButton(text='\u2b05 Тема 2: "Методические рекомендации по проектированию контента электронного курса"', callback_data='pred2')],
    [InlineKeyboardButton(text='\u2b06 Вернуться в главное меню', callback_data='glav1')]
])


themes4 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='\ud83c\udfac 4.1 Начало работы в системе MOODLE', url='https://clck.ru/3CKKtx',callback_data='moodle1')],
    [InlineKeyboardButton(text='\ud83d\udcbb 4.1 Начало работы в системе MOODLE',url='https://clck.ru/3BvcPv', callback_data='moodle')],
    [InlineKeyboardButton(text='\u27a1 Тема 5: "Элементы для работы с информацией"', callback_data='info1')],
    [InlineKeyboardButton(text='\u2b05 Тема 3: "Создание видеолекций для электронного курса"', callback_data='pred3')],
    [InlineKeyboardButton(text='\u2b06 Вернуться в главное меню', callback_data='glav1')]
])


themes5 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='\ud83c\udfac 5.1 Создание и настройка элемента "Файл"',url='https://clck.ru/3CJnnE', callback_data='file1')],
    [InlineKeyboardButton(text='\ud83d\udcbb 5.1 Создание и настройка элемента "Файл"',url='https://clck.ru/3BvcRu', callback_data='file2')],
    [InlineKeyboardButton(text='\ud83c\udfac 5.2 Создание и настройка элемента "Страница"',url='https://clck.ru/3CJnoH', callback_data='map1')],
    [InlineKeyboardButton(text='\ud83d\udcbb 5.2 Создание и настройка элемента "Страница"',url='https://clck.ru/3BvcSv', callback_data='map2')],
    [InlineKeyboardButton(text='\ud83c\udfac 5.2 Работа с элементом "Страница"',url='https://clck.ru/3CJnpX', callback_data='map3')],
    [InlineKeyboardButton(text='\ud83c\udfac 5.3 Создание и настройка элемента "Книга"',url='https://clck.ru/3CJnqQ', callback_data='book1')],
    [InlineKeyboardButton(text='\ud83d\udcbb 5.3 Создание и настройка элемента "Книга"',url='https://clck.ru/3BvcZZ', callback_data='book2')],
    [InlineKeyboardButton(text='\ud83c\udfac 5.4 Создание и настройка элемента "Лекция"',url='https://clck.ru/3CJnqr', callback_data='lection1')],
    [InlineKeyboardButton(text='\ud83d\udcbb 5.4 Создание и настройка элемента "Лекция"',url='https://clck.ru/3BvcaR', callback_data='lection2')],
    [InlineKeyboardButton(text='\ud83c\udfac 5.4 Создание контента в элементе "Лекция"',url='https://clck.ru/3CJnri', callback_data='lection3')],
    [InlineKeyboardButton(text='\ud83c\udfac 5.5 Создание и настройка элемента "Папка"',url='https://clck.ru/3CJnsK', callback_data='papka1')],
    [InlineKeyboardButton(text='\ud83d\udcbb 5.5 Создание и настройка элемента "Папка"',url='https://clck.ru/3BvcdQ', callback_data='papka2')],
    [InlineKeyboardButton(text='\ud83c\udfac 5.6 Создание и настройка элемента "ЭБС Лань"',url='https://clck.ru/3CJntZ', callback_data='ebs_lan1')],
    [InlineKeyboardButton(text='\ud83d\udcbb 5.6 Создание и настройка элемента "ЭБС Лань"',url='https://clck.ru/3Bvez8', callback_data='ebs_lan2')],
    [InlineKeyboardButton(text='\u27a1 Тема 6: "Интерактивные элементы курса"', callback_data='info2')],
    [InlineKeyboardButton(text='\u2b05 Тема 4: "Начало работы в системе MOODLE"', callback_data='pred4')],
    [InlineKeyboardButton(text='\u2b06 Вернуться в главное меню', callback_data='glav1')]
])



themes6 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='\ud83c\udfac 6.1 Создание и настройка элемента "Задание"',url='https://clck.ru/3CKKPM', callback_data='zadanie1')],
    [InlineKeyboardButton(text='\ud83d\udcbb 6.1 Создание и настройка элемента "Задание"',url='https://clck.ru/3BvcgP', callback_data='zadanie')],
    [InlineKeyboardButton(text='\ud83d\udcbb 6.2 Создание тестовых вопросов',url='https://clck.ru/3BvchW', callback_data='test')],
    [InlineKeyboardButton(text='\ud83c\udfac 6.2.1 Создание тестового вопроса типа "Верно/неверно"',url='https://clck.ru/3CKJb8', callback_data='verno')],
    [InlineKeyboardButton(text='\ud83c\udfac 6.2.2 Создание тестового вопроса типа "Множественный выбор"',url='https://clck.ru/3CKJfZ', callback_data='mnvibor')],
    [InlineKeyboardButton(text='\ud83c\udfac 6.2.3 Создание тестового вопроса типа "Короткий ответ"',url='https://clck.ru/3CKJiK', callback_data='korotvet')],
    [InlineKeyboardButton(text='\ud83c\udfac 6.2.4 Создание тестового вопроса типа "На соответствие"',url='https://clck.ru/3CKJn8', callback_data='nasoot')],
    [InlineKeyboardButton(text='\ud83c\udfac 6.2.5 Создание тестового вопроса типа "Числовой"',url='https://clck.ru/3CKJpK', callback_data='chisl')],
    [InlineKeyboardButton(text='\ud83c\udfac 6.2.6 Создание тестового вопроса типа "Вычисляемый"',url='https://clck.ru/3CKJrA', callback_data='vichisl')],
    [InlineKeyboardButton(text='\ud83c\udfac 6.2.7 Создание тестового вопроса типа "Эссе"',url='https://clck.ru/3CKJtj', callback_data='esse')],
    [InlineKeyboardButton(text='\ud83c\udfac 6.2.8 Создание тестового вопроса типа "Выбор пропущенных слов"',url='https://clck.ru/3CKJvY', callback_data='slova')],
    [InlineKeyboardButton(text='\ud83c\udfac 6.2.9 Создание тестового вопроса типа "Перетаскивание в текст"',url='https://clck.ru/3CKJzE', callback_data='text')],
    [InlineKeyboardButton(text='\ud83c\udfac 6.2.10 Создание тестового вопроса типа "Перетаскивание маркеров"',url='https://clck.ru/3CKK3v', callback_data='marker')],
    [InlineKeyboardButton(text='\ud83c\udfac 6.2.11 Создание тестового вопроса типа "Перетаскивание на изображение"',url='https://clck.ru/3CKK5x', callback_data='izobr')],
    [InlineKeyboardButton(text='\ud83c\udfac 6.2.12 Создание табличных задач с помощью тестового вопроса типа "Вложенные ответы (cloze)"',url='https://clck.ru/3CKK7h', callback_data='cloze')],
    [InlineKeyboardButton(text='\ud83c\udfac 6.2.13 Создание тестового вопроса типа "Множественный вычисляемый"',url='https://clck.ru/3CKKAF', callback_data='mnvich')],
    [InlineKeyboardButton(text='\ud83c\udfac 6.2.14 Создание тестового вопроса типа "Простой вычисляемыйй"',url='https://clck.ru/3CKKCo', callback_data='prostvich')],
    [InlineKeyboardButton(text='\ud83c\udfac 6.3 Создание и настройка элемента "Глоссарий"',url='https://clck.ru/3Bw23m', callback_data='gloss1')],
    [InlineKeyboardButton(text='\ud83d\udcbb 6.3 Создание и настройка элемента "Глоссарий"',url='https://clck.ru/3CKKEJ', callback_data='gloss')],
    [InlineKeyboardButton(text='\u27a1 Тема 7: "Элементы для организации взаимодействия между обучающимся"', callback_data='organiz')],
    [InlineKeyboardButton(text='\u2b05 Тема 5: "Элементы для работы с информацией"', callback_data='informationn')],
    [InlineKeyboardButton(text='\u2b06 Вернуться в главное меню', callback_data='glav1')]
])

themes7 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='\ud83c\udfac 7.1 Создание и настройка элемента "Форум"',url='https://clck.ru/3CKJBh', callback_data='forum1')],
    [InlineKeyboardButton(text='\ud83d\udcbb  7.1 Создание и настройка элемента "Форум"',url='https://clck.ru/3BvdLB', callback_data='forum')],
    [InlineKeyboardButton(text='\ud83c\udfac 7.2 Создание и настройка элемента "Чат"', url='https://clck.ru/3CKJQu',callback_data='chat1')],
    [InlineKeyboardButton(text='\ud83d\udcbb  7.2 Создание и настройка элемента "Чат"', url='https://clck.ru/3BvdLx',callback_data='chat')],
    [InlineKeyboardButton(text='\u27a1 Тема 8: "Дополнительные элементы для создания курса"', callback_data='dopelement')],
    [InlineKeyboardButton(text='\u2b05 Тема 6: "Интерактивные элементы курса"', callback_data='predelement')],
    [InlineKeyboardButton(text='\u2b06 Вернуться в главное меню', callback_data='glav1')]
])



themes8 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='\ud83c\udfac 8.1 Создание и настройка элемента "Гиперссылка"',url='https://clck.ru/3CKLZc', callback_data='giper1')],
    [InlineKeyboardButton(text='\ud83d\udcbb 8.1 Создание и настройка элемента "Гиперссылка"',url='https://clck.ru/3BvdZQ', callback_data='giper')],
    [InlineKeyboardButton(text='\ud83c\udfac 8.2 Создание и настройка элемента "Текст и медиа"', url='https://clck.ru/3CKLd4',callback_data='textmedia1')],
    [InlineKeyboardButton(text='\ud83d\udcbb 8.2 Создание и настройка элемента "Текст и медиа"', url='https://clck.ru/3Bvdf2',callback_data='textmedia')],
    [InlineKeyboardButton(text='\ud83c\udfac 8.3 Создание и настройка элемента "Bootstrap Elements"',url='https://clck.ru/3CKLgP', callback_data='bootstrap1')],
    [InlineKeyboardButton(text='\ud83d\udcbb 8.3 Создание и настройка элемента "Bootstrap Elements"',url='https://clck.ru/3BvdfX', callback_data='bootstrap')],
    [InlineKeyboardButton(text='\u27a1 Тема 9: "Экспертиза электронного курса"',callback_data='expert')],
    [InlineKeyboardButton(text='\u2b05 Тема 7: "Элементы для организации взаимодействия между обучающимся"', callback_data='predelement1')],
    [InlineKeyboardButton(text='\u2b06 Вернуться в главное меню', callback_data='glav1')]
])

themes9 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='\ud83d\udcdd 9.1 Экспертиза качества электронного курса"',url='https://clck.ru/3CKNDK', callback_data='expertiza')],
    [InlineKeyboardButton(text='\u27a1 Дополнительные материалы по курсу',callback_data='dopelements')],
    [InlineKeyboardButton(text='\u2b05 Тема 8: "Элементы для организации взаимодействия между обучающимся"', callback_data='elementsvzaim')],
    [InlineKeyboardButton(text='\u2b06 Вернуться в главное меню', callback_data='glav1')]
])

themes10 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='\ud83c\udf10 10.1 Документация по программе "Ассистент"',url='https://clck.ru/3CKNCQ', callback_data='assistent')],
        [InlineKeyboardButton(text='\ud83c\udf10 10.2 Руководство по использованию элемента "Интерактивный контент"', url='https://clck.ru/3CKNBd',callback_data='interaction')],
    [InlineKeyboardButton(text='\ud83d\udcbb 10.3 Создание и настройка элемента "Опрос"',url='https://clck.ru/3CKNAd', callback_data='opros')],
    [InlineKeyboardButton(text='\ud83d\udcbb 10.4 Создание и настройка блоков в Moodle',url='https://clck.ru/3CKN98', callback_data='opros')],
    [InlineKeyboardButton(text='\u2b05 Тема 9: "Экспертиза качества электронного курса"', callback_data='predelement2')],
    [InlineKeyboardButton(text='\u2b06 Вернуться в главное меню', callback_data='glav1')]
])  