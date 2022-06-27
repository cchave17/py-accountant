def runner_app():
    """
    Run main application
    """
    running = True

    while running:
        main_select = 4
        go_back = False

        while go_back == False:
            if main_select == 1:
                if go_back or running == False:
                    break
                go_back = True

            elif main_select == 2:
                running = False
                go_back = True

            elif main_select == 3:
                running = False
                go_back = True
            else:
                running = False
                go_back = True
"""
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
"""