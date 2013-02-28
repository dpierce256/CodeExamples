namespace Game
{
	class GameSpace
	{
		private bool IsPointInPolygon(float[] polyX, float[] polyY, float x, float y)
		{
    		/* 
    		Attempts to determine if a given point (x, y) lies inside the bounds of a polygon described as a series
    		of ordered pairs described in the polyX[] and polyY[] arrays.
    		If (x, y) lies exactly on one of the line segments, this functiom may return True or False.
    		From http://alienryderflex.com/polygon/, converted to C# by David Pierce.
    	
			Arguments:
							float[] polyX	= 		Array that describes the polygon's x coordinates.
    						float[] polyY	= 		Array that describes the polygon's y coordinates.
    						float x         =	 	The x coordinate under test.
    						float y         = 		The y coordinate under test.
	
    		Return values:
    						True			=		Point is inside the polygon.
    						false 			=		Point lies outside polygon OR polygon arrays are of different lengths.
    		*/

    		if (polyX.Length != polyY.Length)
    		{
    			return false;
    		}
        
    		int polySides = polyX.Length;
    		int i = 0;
    		int j = polySides - 1;
    		bool oddNodes = false;

    		while (i < polySides)
    		{
        		if (((polyY[i] < y && polyY[j] >= y) || (polyY[j] < y && polyY[i] >= y)) && (polyX[i] <= x || polyX[j] <= x))
        		{
        	    	if ((polyX[i] + (y- polyY[i]) / (polyY[j] - polyY[i]) * (polyX[j] - polyX[i])) < x)
        	    	{
        	        	oddNodes = !oddNodes;
        	    	}
        		}
        		j = i;
        		i += 1;
    		}
        
    		return oddNodes;

    	}
	}
}