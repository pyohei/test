//問題5−7

import java.io.*;
public class DayReader {
	public static void main (String[] args) {
		BufferedReader reader = new BufferedReader (new InputStreamReader(System.in));
		
		try {
			System.out.println ("0−6の範囲で入力してください。");
			String line = reader.readLine();
			int a = Integer.parseInt(line);
			
			switch (a) {
			case  0:
				System.out.println("Monday");
				break;
				
				case  1:
				System.out.println("Tuesday");
				break;
				
				case  2:
				System.out.println("Wednesday");
				break;
				
				case  3:
				System.out.println("Thursday");
				break;
				
				case  4:
				System.out.println("Friday");
				break;
				
				case  5:
				System.out.println("Saturday");
				break;
				
				case 6 :
				System.out.println("Sunday");
				break;
				
				default :
				System.out.println("規定の数字を入力してください。");
				
				}
			} catch (IOException e) {
				System.out.println(e);
			} catch (NumberFormatException e) {
				System.out.println ("ちゃんと題目を読んでね");
			}
			
		}
	}