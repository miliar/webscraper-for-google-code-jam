 g a r b a g e   =   " e j p   m y s l j y l c   k d   k x v e d d k n m c   r e   j s i c p d r y s i   r b c p c   y p c   r t c s r a   d k h   w y f r e p k y m   v e d d k n k m k r k c d   d e   k r   k d   e o y a   k w   a e j   t y s r   r e   u j d r   l k g c   j v " 
 o r i g i n a l       =   " o u r   l a n g u a g e   i s   i m p o s s i b l e   t o   u n d e r s t a n d   t h e r e   a r e   t w e n t y   s i x   f a c t o r i a l   p o s s i b i l i t i e s   s o   i t   i s   o k a y   i f   y o u   w a n t   t o   j u s t   g i v e   u p " 
 
 m a p p i n g   =   { } 
 
 f o r   i   i n   r a n g e ( l e n ( o r i g i n a l ) ) : 
 	 m a p p i n g [ g a r b a g e [ i ] ]   =   o r i g i n a l [ i ] 
 
 m a p p i n g [ ' q ' ]   =   ' z ' 
 m a p p i n g [ ' z ' ]   =   ' q ' 
 
 
 w i t h   o p e n ( " i n p u t . t x t " ,   " r " )   a s   i n F i l e : 
 	 w i t h   o p e n ( " o u t p u t . t x t " ,   " w " )   a s   o u t F i l e : 
 	 	 i   =   - 1 
 	 	 f o r   l i n e   i n   i n F i l e : 
 	 	 	 i   + =   1 
 	 	 	 i f   i   = =   0 : 
 	 	 	 	 c o n t i n u e 
 	 	 	 
 	 	 	 r e s u l t   =   " " 
 	 	 	 
 	 	 	 f o r   c h a r   i n   l i n e : 
 	 	 	 	 i f   c h a r   i n   m a p p i n g : 
 	 	 	 	 	 r e s u l t   =   r e s u l t   +   m a p p i n g [ c h a r ] 
 	 	 	 
 	 	 	 t e x t   =   " C a s e   # % d :   % s "   %   ( i ,   r e s u l t ) 
 	 	 	 o u t F i l e . w r i t e ( t e x t   +   " \ n " ) 
