package ArrayEx;
/*
 * 배열
 * 정의 : 같은 데이터형의 집합
 * 사용조건 : 배열의 개수보다 하나 작은 인덱스값까지만 접근해서 사용할 수 있다.
 * 배열의 개수를 알고 싶으면 [int Len=배열명.length;]	
 */
public class ArrayEx01 {

	public static void main(String[] args) {
		
		//2의 배수가 있다(0,2,4,6,8,10)
		int a_00=0;
		int a_01=2;
		int a_02=4;
		int a_03=6;
		int a_04=8;
		int a_05=10;
		
		//배열 : 같은 데이터형의 집합
		int[] arr=new int[6];
		arr[0]=0;
		arr[1]=2;
		arr[2]=4;
		arr[3]=6;
		arr[4]=8;
		arr[5]=10;
		
		//0부터 99까지의 값을 100개의 배열변수에 값을 대입하는 예제
		int[] x=new int[100];
		for(int a=0;a<100;a++) {
			x[a]=a*10;
			for(int aa=0; aa<100; aa++) {
				System.out.println(aa+" : "+x[aa]);
			}
		}
		
		//0부터 100까지의 2의 배수값을 trr 배열에 담아주고 출력해주는 코드
		int idx=0;
		int[] trr=new int[100];
		for(int a=0;a<=100;a++) {
			if(a%2==0) {
				trr[idx]=a;
				idx++;
			}
		}
		
		for(int i=0; i<idx; i++) {
			System.out.println("trr["+i+"] : "+trr[i]);
		}
		//0부터 100까지 2의 배수값을 trr배열에 담아주고 출력해주는 코드
		int b=0;
		int c;
		c=0;//변수 초기화
		
		int[] Arr;
		Arr=new int[3]; //배열변수 초기화
		//배열은 배열의 개수보다 하나 작은 인덱스값까지만 접근해서 사용할 수 있다
		
		//Arr[0]=10;
		//Arr[1]=20;
		//Arr[2]=30;
	for(int i=0; i<3; i++) {//총3번이 돌게 됨
		//for문 안에서 i변화는 0~2까지 변한다
		Arr[i]=(i+1)*10;
		System.out.println("Arr["+i+"] = "+Arr[i]);
	}
	//명시적 선언
	int[] A=new int[10];
	int[] B=new int[10];
	
	//암시적 선언
	int[] C= {10,20,30,40,50,60};
//	int[] D;
//	D= {11,22,33,44,55,66}; // <--에러-- 반드시 선언과 동시에 초기화
	
	//명시적+암시적 선언
	int[] E=new int[] {10,20,30,40,50,60};
	int[] F;
	F=new int[] {11,22,33,44,55,66};
	
	}	

}
