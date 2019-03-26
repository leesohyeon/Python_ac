package ForEx;

public class ForEx01 {
	
	 // 0부터 100까지 짝수의 합과 홀수의 합을 구해서 출력

	public static void main(String[] args) {
		int plus=0,minus=0;
		for(int i=0; i<=100; i++) {
			if(i%2==0) {
				plus+=i;
			}
			else
				minus+=i;
		}
			System.out.println("짝수의 합은 "+plus+" 이고 홀수의 합은 "+minus+"이다.");
	}

}
