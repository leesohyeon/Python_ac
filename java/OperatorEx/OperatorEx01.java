package OperatorEx;

public class OperatorEx01 {
	/*
	 * #형변환
	 * 형변환이란 말 그래도 변수나 상서의 데이터타입을 다른 타입으로 바꾸는 것을 의미한다.
	 *
	 * 1, 자동 형변환 (대입으로인한 자동 형변환, 여러 데이터타입이 계산되고 있을 때 큰타입 우선으로 자동 형변환)
	 * byte a = 127;
	 * int b = a;   //(a 타입은 byte 형이지만 대입에 의해 byte -> int 자동 형변환이 된다.)
	 * float c = b; //(b 타입은 int 형이지만 대입에 의해 int -> float 자동 형변환이 된다.)
	 * 계산식이 여러 데이터타입으로 계산되고 있을 때 
	 * 작입타입 -> 큰타입
	 * byte < short < int < long < float < double < char 
	 *
	 * 2, 수동 형변환(Casting, 명시적 형변환, 강제 형변환)
	 * int a = 120;
	 * //byte c = a;   //에러난다.(큰 데이터 타입을 작은 데이터 타입에 대입하려고 했기 때문)
	 * byte b = (byte)a; // 큰 데이터 타입을 작은 데이터 타입에 대입할 때 강제 형변환하면 에러 나지 않는다.
	 * System.out.println(b);
	 *
	 * #상수의 선언
	 * 상수는 프로그램 실행 중에 변경할 수 없는 고정된 값이다.
	 * 사용자가 만든 변수도 상수화 할 수 있다. 변수를 상수화 하는 방법은 다음과 같다.
	 * final 데이터타입 상수명  = 값;
	 * final double PI = 3.14; 
	 */ 
	public static void main(String[] args) {
		int a = 10;
        float b = a / 3.0f;  //(a 타입은 int형이지만 계산에 의해 자동으로 10.0f(float)형으로 형변환이 된다.
        
        int aa = 120;
        //byte c = a;   //에러난다.(큰 데이터 타입을 작은 데이터 타입에 대입하려고 했기 때문)
        byte bb = (byte)aa; // 큰 데이터 타입을 작은 데이터 타입에 대입할 때 강제 형변환하면 에러 나지 않는다.
        System.out.println(bb);
        
        //120 = 30;  //상수는 값을 대입할 수 없다.
        final double PI = 3.14; 
	}

}
