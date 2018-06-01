n=1;
max=1000;
while [ "$n" -le "$max" ]; do
  echo "some text $n" > "s$n"
  n=`expr "$n" + 1`;
done