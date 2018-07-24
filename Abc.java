import java.util.Scanner;
public class Abc {
    public static void main(String args[])
    {
		String s=abcd();
		System.out.println(s);
	}
		public static String abcd()
		{
        Scanner s=new Scanner(System.in);
        String str=s.nextLine();
        String result="";
        char f=Character.toUpperCase(str.charAt(0));
		result=result+f;
        for(int i=1;i<str.length();i++)
        {
            char c=str.charAt(i);
            char previousChar=str.charAt(i-1);
             if(previousChar == ' ')
			 {char e=Character.toUpperCase(c);
			  result=result+Character.toUpperCase(e);
            }
			else
			{
				result=result+str.charAt(i);
			}
            
        }
        return result;
		}
        
    
    
}
