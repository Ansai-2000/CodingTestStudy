class Solution {
    public int solution(String number) {
        char[] charArray = number.toCharArray();
        int answer = 0;
        for(int i=0;i<charArray.length;i++){
            answer += charArray[i] - '0';
        }
        return answer % 9;
    }
}