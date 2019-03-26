package ControlEx;
 
//switch ~ case 문
 
import javax.swing.JOptionPane;
 
public class SwitchCaseEx01 {
 
    public static void main(String[] args) {
        
        int inIQ = Integer.parseInt(JOptionPane.showInputDialog("IQ를 입력해 주세요 : " ));
        
//        if(inIQ == 300)
//        {
//            JOptionPane.showMessageDialog(null, "당신은 천재입니다.");
//        }
//        else if(inIQ == 200)
//        {
//            JOptionPane.showMessageDialog(null, "당신은 무척 똑똑하군요.");
//        }
//        else if(inIQ == 100)
//        {
//            JOptionPane.showMessageDialog(null, "당신은 그냥 평범하군요.");
//        }
//        else if(inIQ == 20)
//        {
//            JOptionPane.showMessageDialog(null, "당신은 사람이 아닙니다.");
//        }
//        else
//        {
//            JOptionPane.showMessageDialog(null, "당신은 지구인이 아니군요!!!");
//        }
        
        // switch ~ case 문은 if ~ else if 문의 다른 표현이다.    
        switch(inIQ) //switch문의 경우 정수 또는 문자(문자열)이어야 한다. *JDK 1.7부터 문자열이 허용되었다.
        {
            case 300:
                JOptionPane.showMessageDialog(null, "당신은 천재입니다.");
                break;
                
            case 200:
                JOptionPane.showMessageDialog(null, "당신은 무척 똑똑하군요.");
                break;
                
            case 100:
                JOptionPane.showMessageDialog(null, "당신은 그냥 평범하군요.");
                break;    
                
            case 20:
                JOptionPane.showMessageDialog(null, "당신은 사람이 아닙니다.");
                break;
                
            default:
                JOptionPane.showMessageDialog(null, "당신은 지구인이 아니군요!!!");
                break;
        }
        
//        char ch = 'r';
//        switch(ch) //switch문의 경우 정수 또는 문자(문자열)이어야 한다. *JDK 1.7부터 문자열이 허용되었다.
//        {
//            case 'a':
//                JOptionPane.showMessageDialog(null, "당신은 천재입니다.");
//                break;
//                
//            case 'b':
//                JOptionPane.showMessageDialog(null, "당신은 무척 똑똑하군요.");
//                break;
//                
//            case 'c':
//                JOptionPane.showMessageDialog(null, "당신은 그냥 평범하군요.");
//                break;    
//                
//            case 'r':
//                JOptionPane.showMessageDialog(null, "당신은 사람이 아닙니다.");
//                break;
//                
//            default:
//                JOptionPane.showMessageDialog(null, "당신은 지구인이 아니군요!!!");
//                break;
//        }
        
    }
 
}