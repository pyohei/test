
// 素数表示

class SosuInput {
	public static void main (String[] args) {
	
	System.out.println ("1番目の素数は 1");
	int a = 2;
	
		for ( int n = 2 ; n <= 9000 ; n++) {
			for (int m = 2 ; m < n ; m++) {
				int p;
				p = n % m;
					
					if ( p == 0) {
						m = n -1;
					} else if (m < n -1) {
					} else {
					 	System.out.println (a +"番目の素数は " + n);
					 	a++ ;
					}
				}
			}
		}
	}