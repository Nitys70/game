
import numpy as np


def game_core_v2(number: int = 1) -> int:
    """Функция для угадывания загаданного числа. 
       Внутри задействуем рекурсивную функцию для сужения результатов поиска искомого числа. 
       После этого используем метод перебора. В функцию встроена инициация ошибки при условии, 
       что менее чем за 20 попыток загаданное программой число не будет угадано.
       
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    
    predict = np.random.randint(1,101)   # Задаем первое число-предположение 
    count = 0  # Задаем счетчик попыток угадывания

    
    def founder(predict):
        """Рекурсвиная функция. Целью этой функции является воспрозведение 10 итераций. 
           В ходе которых число-предположение будет приблежаться к искомому. 
           Оставшиеся 10 попыток (если число не будет угадано в рекурсии) пойдут на перебор. 
           Теория - проделав итерацию 10 раз в диапазоне 100, мы попадем в число не далее
           чем больше/меньше искомого НА 10. В функции применяется метод больше/меньше загаданного числа, 
           в зависимости от которого идут вычисления предполагаемого числа

        Args:
            predict (int): Число-предположение, которое в результате рекурсии приближается к искомому

        Returns:
            int: Максимально приблеженное за 10 итераций число к искомому, оно далее попадает на перебор,
                 или равное, тогда функция завершает свою работу 
        """

        nonlocal count
        
        while predict != number:

            if predict > number:
                
                # Условие останова рекурсии
                if count == 9:     
                    return predict  
                
                count += 1
                
                # Рассчитываем новое число, которое пойдет аргументом функции founder. 
                # в качестве делителя в вычислении применяем count, цель - уменьшение
                # корректировки с каждой итерацией (для исключения "раскачки" нового числа)              
                correction_val = int( predict - predict/(count + 1) - 1 )
                predict = correction_val
                                         
                return founder( predict )
            
            
            elif predict < number:
                
                if count == 9:
                    return predict
                
                count += 1
                correction_val = int( predict + (100 - predict)/(count + 1) + 1 )
                predict = correction_val
                                                        
                return founder(predict)
        
        
        return predict
     
    # Вызов функции для предобработки первоначального числа - предположения    
    pre_result = founder(predict)
    
    # Запускаем цикл перебора для результата работы функции founder(predict)
    # Если founder(predict) нашел искомое число, цикл не запустится  
    while pre_result != number:
        
        if pre_result < number:
            count += 1
            pre_result +=1
        
        elif pre_result > number:
            count += 1
            pre_result -= 1
    
    # Если алгоритм не уложился в 19 попыток, вызовется ошибка 
    if count >= 20:
        raise RuntimeError ('!!! Число попыток угадывания в одной из итераций равно или привысело 20 !!!')
    
   
    return count    



def score_game(game_core_v2) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        game_core_v2 ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    
    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел

    for number in random_array:
        count_ls.append( game_core_v2(number) )
        
    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)


score_game(game_core_v2)     
