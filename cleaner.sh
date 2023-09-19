if [[ "$OSTYPE" == "darwin"* ]]; then
    sed -i "" -e "s/<path.*style=\"stroke:rgb(100.000000%,0.000000%,0.000000%);.*fill: none;\"><\/path>//" mpost/output-svg/65.svg
else
    sed -i -e "s/<path.*style=\"stroke:rgb(100.000000%,0.000000%,0.000000%);.*fill: none;\"><\/path>//" mpost/output-svg/65.svg
fi