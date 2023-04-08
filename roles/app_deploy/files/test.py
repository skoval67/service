import testinfra

def test_port_80(host):
    s = host.socket("tcp://0.0.0.0:80")

    assert s.is_listening
