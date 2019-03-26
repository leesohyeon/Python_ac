package ForEx;
import java.util.Scanner;
public class WhileEx01 {
/*
 * While(조건식)
 * 조건식을 만족하는동안 순회한다
 * while문은 주로 무한루프를 돌릴때 사용한다
 * for문은 주로 순환횟수가 정해져 있는경우 사용한다
 * 
 * while문으로 무한루프를 돌릴 때는 제어문을 적절히 사용해야한다.
 * 제어문: continue, break:
 */
	public static void main(String[] args) {
		Scanner sc= new Scanner(System.in);
		
//		while(true) {
//			System.out.println("계속 진행할까요? (1.예  2.아니요)");
//			int sel=sc.nextInt();
//			if(sel==1) {
//				continue;
//			}
//			if(sel==2) {
//				break;
//			}
//		}
		for(int i=0;i<5;i++) {
			System.out.println(i);
		}
		int j=0;
		while(j<5) {
			System.out.println(j);
			j++;
		}
		
//		  do{
//		  	   //실행되는 부분
//		  }
//		  while(조건식);
		
		int w=1;
		while(5<w) {
			System.out.println("나는 while"+w);
		}
		do {
			System.out.println("나는 do while"+w);
		}
		while(5<w);
		  
		 
		
	}

}
