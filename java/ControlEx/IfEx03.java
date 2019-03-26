package ControlEx;
 
import java.util.Random;
 
import javax.swing.JOptionPane;

/* 
 * Random 클래스
 * Random rd = new Random();
 * int rInt = rd.nextInt(100);  //rInt 0 ~ 100까지 랜덤한 값을 얻어 온다.
 * 주사위의 값은 1부터 ~ 6까지의 값이 나와야 된다.
 * int rand = rd.nextInt(5) + 1;  //0~5  + 1 -> 1~ 6
 */

public class IfEx03 {
 
    public static void main(String[] args) {

    	/*
         * 문제
         * JOptionPane "주사위를 굴렸어요. 지금 나온 숫자는 몇일까요?"
         * 유저로부터 값을 입력 받고
         * 주사위의 숫자를 맞추게 되면 
         * 맞춘경우 --> (주사위값 : %d) 축하합니다. 맞추셨어요. 보상 골드 100
         * 틀린경우 --> (주사위값 : %d) 틀리셨습니다. 다음에 도전해 주세요.
    	 */
//        Random rd = new Random();
//        int rand = rd.nextInt(5) + 1;  
        
//        int InUser = Integer.parseInt(JOptionPane.showInputDialog(
//                                        "주사위를 굴렸어요. 지금 나온 숫자는 몇일까요?"));
//        
//        if(rand == InUser)
//        {
//            String str = "(주사위값 : " + rand + ") 축하합니다. 맞추셨어요. 보상 골드 100";
//            JOptionPane.showMessageDialog(null, a_str);
//        }
//        else 
//        {
//            String str = "(주사위값 : " + rand + ") 틀리셨습니다. 다음에 도전해 주세요.";
//            JOptionPane.showMessageDialog(null, a_str);
//        }
        
        /*
         * JOptionPane "지금 나온 주사위 숫자가 짝수면 1, 홀수면 2를 입력해 주세요."
         * 유저로부터 값을 입력 받고
         * 주사위의 숫자를 맞추게 되면 
         *맞춘경우 --> (주사위값 : %d) 축하합니다. 맞추셨어요. 보상 골드 100
         * 틀린경우 --> (주사위값 : %d) 틀리셨습니다. 다음에 도전해 주세요.    
         */
        Random rd = new Random();
        int rand = rd.nextInt(5) + 1; 
        
        int InUser = Integer.parseInt(JOptionPane.showInputDialog(
                        "지금 나온 주사위 숫자를 예측하여 짝수면 1, 홀수면 2를 입력해 주세요."));
        
        if(InUser == 1 && (rand % 2) == 0)       //짝수인 경우
        {
            String a_str = "(주사위값 : " + rand + ") 축하합니다. 맞추셨어요. 보상 골드 100";
            JOptionPane.showMessageDialog(null, a_str);
        }
        else if(InUser == 2 && (rand % 2) == 1)  //홀수인 경우
        {
            String a_str = "(주사위값 : " + rand + ") 축하합니다. 맞추셨어요. 보상 골드 100";
            JOptionPane.showMessageDialog(null, a_str);
        }
        else
        {
            String a_str = "(주사위값 : " +rand + ") 틀리셨습니다. 다음에 도전해 주세요.";
            JOptionPane.showMessageDialog(null, a_str);
        }
                        
    }
 
}