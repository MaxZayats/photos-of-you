def modify(user_template_name, base_template_name, main_template_name):
    """Фунция модифицирует шаблон main_template_name.

    В main_template_name добавляется скрипт и пользовательский шаблон.

    """
    user_template = open('templates/'+user_template_name, 'r')
    base_template = open('templates/'+base_template_name, 'r')
    main_template = open('templates/'+main_template_name, 'w')

    main_template.write(
        user_template.read() + base_template.read()
    )
