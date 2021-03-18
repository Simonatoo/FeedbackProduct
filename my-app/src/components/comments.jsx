import React from 'react'
import './styles/comments.css'

function Comments(){

    var comment_title = "Título aqui"
    var comment_desc = "Texto descritivo aqui asid aspdpas kopaskdopakdopa sopas kopaskdopasopda ksopkdas"

    return(
        <div className="comment-body">
            <div className="comment-title">
                <h2>
                    Comments
                </h2>
            </div>
            <div className="comment-margim">
                <div className="comment-text">
                    <h3>
                        {comment_title}
                    </h3>
                    <p>
                        {comment_desc}
                    </p>
                </div>
            </div>
        </div>
    )
}

export default Comments