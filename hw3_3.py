def function_name(
    search: str, 
    status: bool, 
    *args: int, 
    **kwargs: str
) -> list[int] | str:
    """
    Обрабатывает аргументы в зависимости от параметров search и status.
    
    Параметры:
        search (str): Режим работы функции ("args" или "kwargs")
        status (bool): Флаг для режима args (True - числа, False - строки)
        @args (int): Произвольное количество позиционных аргументов
        **kwargs (str): Произвольное количество именованных аргументов
    
    Возвращает:
        list[int] | str: 
            Если search="args" и status=True: список целых чисел
            Если search="args" и status=False: строка из всех аргументов
            Если search="kwargs": строка с ключами и значениями
    
    Исключения:
        ValueError: Если search не равен "args" или "kwargs"
    """
    result: list[int] = []
    result_2: str = ""
    
    if search == "args":
        if status:
            for i in args:
                if isinstance(i, int):
                    result.append(i)
            return result
        else:
            for i in args:
                result_2 += f"{i}"
            return result_2
    elif search == "kwargs":
        for k, v in kwargs.items():
            result_2 += f"Key: {k}, Value: {v}"
        return result_2
    else:
        raise ValueError("Error for search")
