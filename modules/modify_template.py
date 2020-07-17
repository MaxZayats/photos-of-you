def modify(user_template_name, base_template_name, main_template_name):
    """The function modifies the "main_template_name" template.

    A script and a custom template are added to the "main_template_name" template.

    """
    user_template = open('server/templates/'+user_template_name, 'r')
    base_template = open('server/templates/'+base_template_name, 'r')
    main_template = open('server/templates/'+main_template_name, 'w')

    main_template.write(
        user_template.read() + base_template.read()
    )
