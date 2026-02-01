from aiogram.fsm.state import State, StatesGroup

class ZakatStates(StatesGroup):
    asking_amount = State()
