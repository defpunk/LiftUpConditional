def lift_up_conditional(a: bool, b: bool) -> str:
    if a:
        if b:
            return "ATrueBTrue"
        else:
            return "ATrueBFalse"
    else:
        if b:
            return "AFalseBTrue"
        else:
            return "AFalseBFalse"