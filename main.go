package main
import (
    "net/http"
    "github.com/gin-gonic/gin"
)

func main()  {
	r := gin.Default()
 	r.GET("/", func(c *gin.Context) {
        c.JSON(http.StatusOK, gin.H{"msg": "Go Server is running~"})
    })
	r.Run(":9000")
}