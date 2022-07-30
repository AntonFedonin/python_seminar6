
import model_sub
import model_mult
import model_sum
import view


def button_click():
    value_a = view.get_value()
    operator = view.get_operation()
    value_b = view.get_value()
    if operator == '+':
        model_sum.init(value_a, value_b)
        result = model_sum.do_it()
        title = 'Сумма'
    elif operator == '-':
        model_sub.init(value_a, value_b)
        result = model_sub.do_it()
        title = 'Разница'
    if operator == '*':
        model_mult.init(value_a, value_b)
        result = model_mult.do_it()
        title = 'Произведение'
    # if operator == '/':
    #     model_sum.init(value_a, value_b)
    #     result = model_sum.do_it()
    view.view_data(result, title)
