//問題4-3
import java.io.*;

public class NowTime {
	public static void main (String[] args) {
		BufferedReader reader = new BufferedReader (new InputStreamReader (System.in));
		
		System.out.println ("現在の時刻は(２４時間で時のみ表示)");

		
		try {
			String line = reader.readLine();
			int n = Integer.parseInt(line);
		
			if ( n >=0 && n<= 11 ) {
			System.out.println ("おっはよ");
			
			} else if ( n == 12 ) {
			System.out.println ("お昼だよ");
			
			} else if ( n >= 13 && n <=18 ) {
			System.out.println ("こんちわ");
			
			} else if ( n >= 19 && n <=23 ) {
			System.out.println ("こんばんわ");
			}
			
			} catch (IOException e) {
				System.out.println ( e );
			} catch (NumberFormatException e) {
				System.out.println("時刻の範囲を超えています");
			}
				
			}
		}
	