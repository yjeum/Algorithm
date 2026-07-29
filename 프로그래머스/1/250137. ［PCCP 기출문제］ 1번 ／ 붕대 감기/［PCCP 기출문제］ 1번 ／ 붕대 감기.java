class Solution {
    public int solution(int[] bandage, int health, int[][] attacks) {
        
        int curHealth = health;
        int beforeTime = 0;
        
        for (int[] attack : attacks) {
            int gap = attack[0] - beforeTime - 1;
            
            // 현재 체력 회복
            curHealth = Math.min(curHealth + gap * bandage[1] + (gap / bandage[0]) * bandage[2], health);
                
            // 몬스터 공격
            curHealth -= attack[1];
                
            if (curHealth <= 0) {
                return -1;
            };
            
            beforeTime = attack[0];
        }
        
        return curHealth;
    }
}