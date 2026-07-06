import main


def run():
    # Basic checks that don't require interactive input
    assert hasattr(main, 'QUESTIONS'), "QUESTIONS not found in main"
    assert len(main.QUESTIONS) >= 5, "Not enough questions"
    # Test lifeline functions run without error
    _ = main.lifeline_5050(main.QUESTIONS[0])
    main.lifeline_audience(main.QUESTIONS[0])
    print("Smoke test passed: QUESTIONS present and lifelines callable")


if __name__ == '__main__':
    run()
