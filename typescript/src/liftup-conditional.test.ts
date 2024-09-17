import liftupConditional from './liftup-conditional'

describe('liftupConditional', () => {
    it('should return ATrueBTrue when input is true, true', () => {
        expect(liftupConditional(true, true)).toBe('ATrueBTrue')
    });
    it('should return ATrueBFlase when input is true, false', () => {
        expect(liftupConditional(true, false)).toBe('ATrueBFalse')
    });
    it('should return AFalseBTrue when input is false, true', () => {
        expect(liftupConditional(false, true)).toBe('AFalseBTrue')
    });
    it('should return AFalseBFalse when input is false, false', () => {
        expect(liftupConditional(false, false)).toBe('AFalseBFalse')
    });
})