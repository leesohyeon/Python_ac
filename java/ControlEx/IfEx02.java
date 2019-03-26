package ControlEx;
 
import javax.swing.JOptionPane;
 
/*
 * 국어점수  JOptionPane
 * 영어점수
 * 수학점수를 입력받고
 * 총점과 평균을 구한 후
 * 평균값으로 적당한 문구를 출력해 주자!!
 *
 * 평균값 80.0f <= 
 * "잘했다. 그레잇~ 총점(280) 평균(97.23)"
 * else if 평균값 60.0f <=
 * "소심. 그레잇~ 총점(xxx) 평균(xx.xx)"
 * else if 평균값 40.0f <= 
 * "스튜핏~ 총점(xxx) 평균(xx.xx)"
 * else if 평균값 20.0f <= 
 * "매우 스튜핏~ 총점(xxx) 평균(xx.xx)"
 * else
 * "집에가라. 스튜핏~ 총점(xxx) 평균(xx.xx)"
 */
public class IfEx02 {
 
    public static void main(String[] args) {
 
        int Kor = Integer.parseInt(JOptionPane.showInputDialog(
                                        "국어점수를 입력해 주세요"));
        
        int Eng = Integer.parseInt(JOptionPane.showInputDialog(
                                        "영어점수를 입력해 주세요"));
        
        int Math = Integer.parseInt(JOptionPane.showInputDialog(
                                        "수학점수를 입력해 주세요"));
        
        int Total = Kor + Eng + Math;
        float Avg = Total / 3.0f;
        
//        if(80.0f <= Avg)
//        {
//            System.out.printf("잘했다. 그레잇~ 총점(%d) 평균(%.2f)\n", Total, Avg);
//        }
//        else if(60.0f <= Avg)
//        {
//            System.out.printf("소심. 그레잇~ 총점(%d) 평균(%.2f)\n", Total, Avg);
//        }
//        else if(40.0f <= Avg)
//        {
//            System.out.printf("스튜핏~ 총점(%d) 평균(%.2f)\n", Total, Avg);
//        }
//        else if(20.0f <= Avg)
//        {
//            System.out.printf("매우. 스튜핏~ 총점(%d) 평균(%.2f)\n", Total, Avg);
//        }
//        else
//        {
//            System.out.printf("집에가라. 스튜핏~ 총점(%d) 평균(%.2f)\n", Total, Avg);
//        }
        
        if(80.0f <= Avg)
        {
            System.out.printf("잘했다. 그레잇~ 총점(%d) 평균(%.2f)\n", Total, Avg);
        }
        if(60.0f <= Avg && Avg < 80.0f)
        {
            System.out.printf("소심. 그레잇~ 총점(%d) 평균(%.2f)\n", Total, Avg);
        }
        if(40.0f <= Avg && Avg < 60.0f)
        {
            System.out.printf("스튜핏~ 총점(%d) 평균(%.2f)\n", Total, Avg);
        }
        if(20.0f <= Avg && Avg < 40.0f)
        {
            System.out.printf("매우. 스튜핏~ 총점(%d) 평균(%.2f)\n", Total, Avg);
        }
        if(Avg < 20.0f)
        {
            System.out.printf("집에가라. 스튜핏~ 총점(%d) 평균(%.2f)\n", Total, Avg);
        }
        
    }
 
}