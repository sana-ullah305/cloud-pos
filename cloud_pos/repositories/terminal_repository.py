class TerminalRepository:
    terminals = []

    @classmethod
    def save_terminal(cls, terminal):
        cls.terminals.append(terminal)

    @classmethod
    def get_terminal_by_id(cls, terminal_id):
        for terminal in cls.terminals:
            if terminal.terminal_id == terminal_id:
                return terminal
        return None
