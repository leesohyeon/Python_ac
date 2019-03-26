package ForEx;
import java.util.Scanner;
/*
 * 영화예매 프로그램
 * 
 * 1.범죄도시 1관
 * 2.1987	2관
 * 3.코코	3관
 * 4.신과함께	4관
 * 
 * 영화를 선택해주세요 : 
 * 
 * 인원수를 입력해주세요(1인당 9000원) :
 * 
 * 시간을 선택해주세요 : 1.(8:00)  2.(10:40)  3.(13:15)  4.(15:50)  5.(23:20)
 * --가격계산--
 * 선택한 영화는 코코 3관 3명 27000우너 입니다
 * 돈을 입력해주세요 : 
 * (부족할 경우) 돈이 부족합니다 다시 입력해주세요
 * 
 * 당신은 코코 3관 3명 10:40을 예매하셨습니다 . 잔돈 2500을 받으세요
 */
public class Theater {

	public static void main(String[] args) {
		while(true) {
			int money=0,change=0;
			String moviesel="",timesel="";
		Scanner sc=new Scanner(System.in);
		System.out.print(" [영화예매 프로그램]\n" + 
				" 1.범죄도시	1관\n" + 
				" 2.1987		2관\n" + 
				" 3.코코		3관\n" + 
				" 4.신과함께	4관\n" + 
				"\n"+
				"* 영화를 선택해주세요 : ");
		int movie=sc.nextInt();
		System.out.println();
		if(movie==1) {
			moviesel="'범죄도시' [1관]";
		}
		else if(movie==2) {
			moviesel="'1987' [2관]";
		}
		else if(movie==3) {
			moviesel="'코코' [3관]";
		}
		else if(movie==4) {
			moviesel="'신과함께' [4관]";
		}
		System.out.print("* 인원수를 입력해주세요 : ");
		int people=sc.nextInt();
		System.out.println();
		money=people*9000;
		System.out.print("* 시간을 선택해주세요  1.(8:00)  2.(10:40)  3.(13:15)  4.(15:50)  5.(23:20) :");
		int time = sc.nextInt();
		System.out.println();
		if (time==1) {
			timesel="(8:00)";
		}
		else if (time==2) {
			timesel="(10:40)";
		}
		else if (time==3) {
			timesel="(13:15)";
		}
		else if (time==4) {
			timesel="(15:50)";
		}
		else if (time==5) {
			timesel="(23:20)";
		}
		
		System.out.println("선택한 영화는 "+moviesel+" "+people+"명, "+money+"원 입니다.");
		System.out.println();
		while(true) {
		System.out.print("돈을 입력해주세요 :");
		int pay=sc.nextInt();
		if(pay<money) {
			System.out.println("돈이 부족합니다. 다시 입력해주세요");
			System.out.println();
			continue;
				}
		else {
			change=pay-money;
			break;
		}	
		}
		System.out.println();
		System.out.println("당신은 "+moviesel+" "+people+" "+timesel+"예매하셨습니다. 잔돈 "+change+"원을 받으세요");
		System.out.println();
		
		System.out.println("한번 더 예매하시겠습니까? (Y/N)");
		String sel=sc.next();
		if(sel=="y") {
			continue;
		}
		else {
			System.out.println("이용해주셔서 감사합니다. 예매시스템을 종료합니다");
			break;
		}
		}
	}

}
