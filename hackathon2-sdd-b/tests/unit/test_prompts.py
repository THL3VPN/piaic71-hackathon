from cli import prompts


def test_collect_task_inputs_uses_mock(questionary_mock):
    questionary_mock.calls['text'] = 'Title A'
    questionary_mock.calls['select'] = 'high'
    questionary_mock.calls['confirm'] = True

    # Preseed return values for ask()
    questionary_mock.calls.update({'text': 'Title A', 'select': 'high', 'confirm': True})

    task = prompts.collect_task_inputs(title=None, priority=None, notes=None)
    assert task['title'] == 'Title A'
    assert task['priority'] == 'high'
    assert task['status'] == 'pending'


def test_stub_list_tasks_filters():
    sample = prompts.stub_list_tasks(priority='high', status='pending')
    assert all(t['priority'] == 'high' for t in sample)
    assert all(t['status'] == 'pending' for t in sample)
