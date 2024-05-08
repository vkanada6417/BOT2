from random import choice
help = [
    "Советы по тому как стать экологичнее: $-how_to_ec"
    "Сколько что разлогается: $-whenraz"
    "Список команд: $-com_help"
    
]
def helpp():
    return help
    
 
eco_facts = [
    "Посадить дерево",
    "Построить скворечник, синичник",
    "Повесить и своевременно наполнять кормушку, поилку для птиц",
    "Ездить волонтером на проекты по спасению, восстановлению, учету животных",
    "Поддерживать фонды помощи животным",
    "Реже пользоваться кондиционером",
    "Убавлять индивидуальное отопление",
    "Покупать энергосберегающие приборы",
    "Сажать деревья",
    "Выбрать электротранспорт",
    "Больше ездить на велосипеде и ходить пешком",
    "Сортировать мусор",
    "Раздавать и продавать ненужные вещи, уменьшая количество мусора",
    "Устраивать и посещать фримаркеты для обмена вещами",
    "Пустую пластиковую упаковку, остатки ткани и прочее пускать на поделки",
    "В походе ходить только по тропам",
    "Не повреждать и не рвать без нужды растения, не ломать ветки",
    "Не шуметь, не включать громкую музыку",
    "Не кормить диких животных",
    "Не трогать птиц, насекомых",
    "Не оставлять надписи на камнях и прочих природных объектах",
    "Для разведения костра использовать старые кострища",
    "Ненужный костер затушить и засыпать землей",
    "Не разводить костры там, где это запрещено",
    "Не использовать на природе бытовую химию",
    "Закапывать органические отходы",
    "После отдыха на природе забирать с собой мусор",
    "Собирать мусор в любимых уголках отдыха - в одиночку или с коллективом единомышленников",
    "Отправиться волонтером на уборку мусора в популярных туристических местах",
    "Прививать детям и окружающим любовь к природе - как сделать это интересно и ненавязчиво"
]

def random_fact():
    return str(choice(eco_facts))

rco_sht = [
    "Бумажные пакеты экологичнее полиэтиленовых -- Производство одного бумажного пакета равнозначно производству"
    "нескольких полиэтиленовых по объему затраченных ресурсов и генерированию вредных выбросов",
    'Электромобили не вредят природе -- В отличие от автомобилей с двигателями внутреннего сгорания'
    '(ДВС) электромобили действительно не выбрасывают вредные газы в атмосферу и работают сравнительно'
    'тише, но это ещё не значит, что они являются безопасным экологическим решением для планеты.'
    'Для того чтобы получить электричество чаще всего сжигают топливо => выделяется столько же вредных веществ или больше.',
    "Вырубку старых лесов можно компенсировать посадкой молодого леса -- Аналогично почкам и печени в организме"
    "человека леса выполняют функции фильтра — очищают воздух и защищают почву от эрозий. Компенсировать"
    "вырубку одного взрослого дерева пятью молодыми невозможно, потому что новые саженцы не смогут в той же"
    "мере охлаждать и увлажнять воздух, поглощать пыль и уж точно не могут служить кормовой базой и местом обитания фауны",
    'Покупая товары с маркировками «эко», «био», «экологический», «натуральный», я помогаю сохранять природу -- большинство'
    'продуктов, который видит потребитель на полках магазинов с маркировкой «эко», «био» и т.п. не являются гарантией того,'
    'что продукт экологичен и безопасен.'
]

def eko_mith():
    return str(choice(rco_sht))


razlog = [
    'Пищевые отходыдо 1 месяца'
    'Газетная бумага до 1 года'
    'Картонные коробки до 1 года'
    'Бумага 2 года'
    'Доски деревянные до- 10 лет'
    'Железная арматура до 10 лет'
    'Железные банки до 10 лет'
    'Старая обувьдо 10 лет'
    'Обломки кирпича, бетона до 100 лет'
    'Автоаккумуляторы до 100 лет'
    'Фольга до 100 лет'
    'Жестяная банка до 90 лет'
    'Электрические батарейки до 100 лет'
    'Резиновые покрышки более 100 лет'
    'Пластиковые бутылки более 100 лет'
    'Полиэтиленовая пленка 200 лет'
    'Алюминиевые банки 500 лет'
    'Стекло более 1000 лет'
]

def raz_log():
    return str(choice(razlog))