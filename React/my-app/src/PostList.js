// src/PostList.js
import React, { Component } from "react";
import PostItem from './PostItem';

class PostList extends Component {
    render() {
        // SỬA LỖI Ở ĐÂY: 'Posts' -> 'posts' (viết thường)
        const { posts } = this.props; 

        return (
            <div className="post-list">
                <h2>Bài viết</h2>
                {posts.map((post) => (
                    <PostItem key={post.id} title={post.title} content={post.content} />
                ))}
            </div>
        );
    }
}

export default PostList;