from State import State


class Action:

    @staticmethod
    def change_between_two_pipe(state: State, pipe_src_ind: int, pipe_dest_ind: int):
        state.pipes[pipe_dest_ind].add_ball(state.pipes[pipe_src_ind].remove_ball())
