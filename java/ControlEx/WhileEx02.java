package ControlEx;
 
import javax.swing.JOptionPane;
 
/*
 * 문제
 * 잔돈 없는 자판기
 * 
 * 사탕   500
 * 새우깡 1000
 * 콜라   1500
 * 컵라면 2000
 * 
 * JOptionPane 금액을 입력해 주세요 : 
 *
 * 예외처리 500원 이하나 2000원이상을 입력하면
 * --> 500원보다 크고 2000원보다 작은 금액만 받습니다.
 * --> break;
 *
 * 정확한 돈을 입력해야 물건을 준다.
 * 500 -> 사탕을 받으세요. (출력)
 * 1000 -> 새우깡을 받으세요.
 * 1500 -> 콜라를 받으세요.
 * 2000 -> 컵라면을 받으세요.
 * 중간값을 입력하면 잔돈없어요. 다음에 또 구입해 주세요.
 *
 * while(true) 무한 반복
 */
 
public class WhileEx02 {
 
    public static void main(String[] args) {
    
        System.out.println("사탕 500");
        System.out.println("새우깡 1000");
        System.out.println("콜라 1500");
        System.out.println("컵라면 2000");    
        
        while(true)
        {        
            int Value = Integer.parseInt(JOptionPane.showInputDialog(
                    "금액을 입력해 주세요."));
    
            if(Value < 500 || 2000 < Value) //예외처리
            {
                JOptionPane.showMessageDialog(null, "500원보다 크고 2000원보다 작은 금액만 받습니다.");
                break;
            }
            
            if(Value == 500)
            {
                JOptionPane.showMessageDialog(null, "사탕을 받으세요.");
            }            
            else if(Value == 1000)
            {
                JOptionPane.showMessageDialog(null, "새우깡을 받으세요.");
            }
            else if(Value == 1500)
            {
                JOptionPane.showMessageDialog(null, "콜라를 받으세요.");
            }
            else if(Value == 2000)
            {
                JOptionPane.showMessageDialog(null, "컵라면을 받으세요.");
            }
            else
            {
                JOptionPane.showMessageDialog(null, "잔돈없어요. 다음에 또 구입해 주세요.");
            }
            
        }//while(true)
 
    }
 
}