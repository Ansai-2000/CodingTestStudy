class Solution {
    public String solution(int age) {
        String answer = String.valueOf(age);
        char[] arr = answer.toCharArray();
        String result = "";
        for(int i=0;i<arr.length;i++){
            result += (char)('a' + arr[i] - '0');
        }
        return result;
    }
}