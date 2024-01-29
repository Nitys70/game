
import numpy as np


def game_core_v2(number: int = 1) -> int:
    """Сначала устанавливаем любое random число, а потом уменьшаем
    или увеличиваем его в зависимости от того, больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток
       
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    
    predict = np.random.randint(1,101)
    count = 0

    
    def founder(predict):

        nonlocal count
        
        while predict != number:

            if predict > number:
                
                if count == 9:
                    return predict  
                
                count += 1              
                correction_val = int( predict - predict/(count + 1) - 1 )
                predict = correction_val
                                         
                return founder( predict )
            
            
            elif predict < number:
                
                if count == 9:
                    return predict
                
                count += 1
                correction_val = int( predict + (100-predict)/(count+1) + 1 )
                predict = correction_val
                                                        
                return founder(predict)
        
        return predict
     
        
    pre_result = founder(predict)
      
    while pre_result != number:
        
        if pre_result < number:
            count += 1
            pre_result +=1
        
        elif pre_result > number:
            count += 1
            pre_result -= 1
    
    if count >= 20:
        raise RuntimeError ('!!! Число попыток угадывания в одной из итераций равно или привысело 20 !!!')
    
   
    return count    



def score_game(game_core_v2) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

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