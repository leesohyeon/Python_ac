package ArrayEx;

public class ArrayEx02 {

	public static void main(String[] args) {
		int[] Score= {11,22,45,6,77,88,94,100,45};
		//총점과 평균값을 for문을 이용하여 출력해주세요
		int  Len=Score.length;
		int tot=0;
		float avg=0.0f;
		for(int i=0; i<Len;i++) {
			tot+=Score[i];
		}
		avg=tot/Len;
		System.out.println("배열값의 총합은 "+tot+"이며 평균은 "+avg+"입니다");
	
		//while 문으로 
		
	
		//0부터 100까지의 3의 배수값을 배열에 담고 출력해보자
		int[] arr=new int[100];
		int idx=0;
		for(int a=0; a<=100; a++) {
			if(a%3==0) {
				arr[idx]=a;
				idx++; // 맨 마지막은 34개가 될것이다.
			}
		}
		for(int b=0; b<idx; b++) {
			System.out.println("arr["+b+"]"+arr[b]);
		}
		
		//0부터 100까지 3의 배수값을 배열에 담고 출력을 해보자
		//배열에 다음과 같이 담아보자
		//[0] 0+1  [1] 2+3  [2] 4+5  [3] 6+7....
		int inx=0;
		int[] v=new int[100];
		
		for(int dd=0; dd<=100; dd++) {
			if(dd%2==1) {
				v[inx]=(dd-1)+dd;
				inx++;
			}
		}
		for(int dd=0; dd<inx; dd++) {
			System.out.println("v["+dd+"] = "+v[dd]);
		}
		
		//배열에 다음과 같이 담아보자
		//[0] 0+1+2  [1] 3+4+5 [2] 6+7+8  ....
		int Idx=0;
		int[] vv=new int[100];
		
		for(int cc=0; cc<=100; cc++) {
			if(cc%3==1) {
				vv[Idx]=(cc-1)+cc+(cc+1);
				Idx++;
			}
		}
		for(int cc=0; cc<Idx; cc++) {
			System.out.println("vv["+cc+"] = "+vv[cc]);
		}
		
		// 문제  swap
		int[] sw=new int[100];
		for(int ii=0; ii<100; ii++) {
			sw[ii]=ii;//<-- [0]=0 [1]=1 [2]=2 [3]=3.....
		}
		//[0]<-->[1]   [2]<-->[3]
		// 1      0     3      2
		for(int ii=0; ii<100; ii++) {
		int temp=0;
		if(ii%2==1) {
		temp=sw[ii-1];
		sw[ii-1]=sw[ii];
		sw[ii]=temp;
		}
		for(int hh=0;hh<100;hh++) {
		System.out.println("sw ["+hh+"] = "+sw[hh]);
		
		}
	}
		
	}
}
	
