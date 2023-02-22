/**
 * @param {number[]} weights
 * @param {number} days
 * @return {number}
 */

function check(m,weights,days)
{
    let i =0;
    while(i<weights.length)
        {
            let s = 0;
            while(i<weights.length && (s+weights[i]<=m))
                {
                    s+=weights[i];
                    ++i;
                }
    
            days--;
            if(days<0)return 0;
        }

    return 1;
}
var shipWithinDays = function(weights, days) {
    let l =1;
    let r = 0;
    for(let i = 0;i<weights.length;++i)
        r+=weights[i];
    
    let ans = r;
    while(l<=r)
        {
            let m = (l+r)/2;
        m = parseInt(m);
            if(check(m,weights,days))
                r = m-1,ans =m;
            else l = m+1;
        }
    return ans;
};