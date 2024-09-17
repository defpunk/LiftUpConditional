export default function liftUpConditional(a: boolean, b: boolean): string {
    if (a) {
        if (b) {
            return "ATrueBTrue"
        } else {
            return "ATrueBFalse"
        }
    } else {
        if (b) {
            return "AFalseBTrue"
        }
        else {
            return "AFalseBFalse"
        }
    }
}
